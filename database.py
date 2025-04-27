import sqlite3
import datetime

class DatabaseManager:
    """
    Manage SQLite operations for optimal samples.
    """
    def __init__(self, db_path='optimal_samples.db'):
        self.db_path = db_path
        self.setup_database()

    def setup_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Create results table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                m INTEGER,
                n INTEGER,
                k INTEGER,
                j INTEGER,
                s INTEGER,
                run_id TEXT,
                num_results INTEGER,
                samples TEXT,
                timestamp TEXT,
                computation_time REAL
            )
        ''')
        # Create result groups table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS result_groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                result_id INTEGER,
                group_num INTEGER,
                group_samples TEXT,
                FOREIGN KEY (result_id) REFERENCES results(id)
            )
        ''')
        conn.commit()
        conn.close()

    def save_result(self, m, n, k, j, s, run_id, samples, computation_time, groups):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Insert into results
        cursor.execute('''
            INSERT INTO results (m, n, k, j, s, run_id, num_results, samples, timestamp, computation_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            m, n, k, j, s, run_id,
            len(groups),
            ','.join(str(x) for x in samples),
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            computation_time
        ))
        result_id = cursor.lastrowid
        # Insert groups
        for idx, grp in enumerate(groups, 1):
            cursor.execute('''
                INSERT INTO result_groups (result_id, group_num, group_samples)
                VALUES (?, ?, ?)
            ''', (result_id, idx, ','.join(str(x) for x in grp)))
        conn.commit()
        conn.close()
        return result_id

    def get_all_results(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, m, n, k, j, s, num_results, timestamp, computation_time
            FROM results
            ORDER BY timestamp DESC
        ''')
        rows = cursor.fetchall()
        conn.close()
        return rows

    def search_results(self, term):
        pattern = f"%{term}%"
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, m, n, k, j, s, num_results, timestamp, computation_time
            FROM results
            WHERE LOWER(timestamp) LIKE ? OR m LIKE ? OR n LIKE ? OR k LIKE ? OR j LIKE ? OR s LIKE ?
            ORDER BY timestamp DESC
        ''', (pattern, pattern, pattern, pattern, pattern, pattern))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def load_result(self, result_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT m, n, k, j, s, samples, computation_time
            FROM results
            WHERE id = ?
        ''', (result_id,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return None
        m, n, k, j, s, samples_str, computation = row
        # Load groups
        cursor.execute('''
            SELECT group_samples FROM result_groups
            WHERE result_id = ?
            ORDER BY group_num
        ''', (result_id,))
        groups = [ [int(x) for x in r[0].split(',')] for r in cursor.fetchall() ]
        conn.close()
        return {
            'params': (m, n, k, j, s),
            'samples': [int(x) for x in samples_str.split(',')],
            'computation_time': computation,
            'groups': groups
        }

    def delete_result(self, result_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM result_groups WHERE result_id = ?', (result_id,))
        cursor.execute('DELETE FROM results WHERE id = ?', (result_id,))
        conn.commit()
        conn.close()
