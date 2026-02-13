"""
Django management command to reset PostgreSQL sequences for auto-increment fields.

This fixes the "duplicate key value violates unique constraint" error that occurs
when sequences get out of sync with the actual data in tables.

Usage:
    python manage.py reset_sequences
"""

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Reset PostgreSQL sequences for all tables to match current max IDs'

    def handle(self, *args, **options):
        """Execute the sequence reset"""
        
        with connection.cursor() as cursor:
            # List of tables and their primary key sequence names
            sequences = [
                ('sql_trip', 'sql_trip_trip_id_seq'),
                ('sql_trip_day', 'sql_trip_day_day_id_seq'),
                ('sql_trip_item', 'sql_trip_item_item_id_seq'),
                ('sql_item_dependency', 'sql_item_dependency_dependency_id_seq'),
                ('sql_share_link', 'sql_share_link_link_id_seq'),
                ('sql_vote', 'sql_vote_vote_id_seq'),
                ('sql_trip_review', 'sql_trip_review_review_id_seq'),
                ('sql_user_media', 'sql_user_media_media_id_seq'),
            ]
            
            self.stdout.write(self.style.WARNING('Resetting sequences...'))
            
            for table_name, sequence_name in sequences:
                try:
                    # Get the primary key column name (first word in sequence name after table)
                    pk_column = sequence_name.replace(f'{table_name}_', '').replace('_seq', '')
                    
                    # Check current sequence value
                    cursor.execute(f"SELECT last_value FROM {sequence_name}")
                    old_value = cursor.fetchone()[0]
                    
                    # Get max ID from table
                    cursor.execute(f"SELECT MAX({pk_column}) FROM {table_name}")
                    result = cursor.fetchone()
                    max_id = result[0] if result[0] is not None else 0
                    
                    # Reset sequence (use 1 as minimum for empty tables)
                    if max_id == 0:
                        cursor.execute(f"SELECT setval('{sequence_name}', 1, false)")
                    else:
                        cursor.execute(f"SELECT setval('{sequence_name}', {max_id}, true)")
                    
                    # Get new value
                    cursor.execute(f"SELECT last_value FROM {sequence_name}")
                    new_value = cursor.fetchone()[0]
                    
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✓ {table_name}.{pk_column}: {old_value} → {new_value} (max: {max_id})'
                        )
                    )
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'✗ {table_name}: {str(e)}')
                    )
            
            self.stdout.write(self.style.SUCCESS('\nAll sequences reset successfully!'))
