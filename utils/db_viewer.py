import sqlite3
import sys
from pathlib import Path

def view_sqlite_db(db_path):
    """View the contents of a SQLite database."""
    if not Path(db_path).exists():
        print(f"Database file not found: {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("No tables found in database.")
            return

        print(f"\nFound {len(tables)} tables:")
        for table in tables:
            table_name = table[0]
            print(f"\n=== Table: {table_name} ===")
            
            # Get column names
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            column_names = [col[1] for col in columns]
            print("Columns:", ", ".join(column_names))
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            print(f"Row count: {count}")
            
            # Show first 5 rows
            if count > 0:
                print("\nFirst 5 rows:")
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python db_viewer.py <path_to_sqlite_db>")
        sys.exit(1)
    
    view_sqlite_db(sys.argv[1])