"""
Runs the full pipeline end to end: python run_pipeline.py

Before running: copy .env.example to .env, add transactions.csv to
data/raw/, and download the Postgres JDBC driver into jars/.
"""

from pipeline import (
    step1_create_database,
    step2_create_schemas,
    step3_profile_data,
    step4_load_raw_data,
    step5_transform_data,
    step6_build_warehouse,
    step7_create_analytics_views,
)

STEPS = [
    ("Create database", step1_create_database),
    ("Create schemas & tables", step2_create_schemas),
    ("Profile raw data", step3_profile_data),
    ("Load raw data into Postgres", step4_load_raw_data),
    ("Run PySpark transformations", step5_transform_data),
    ("Build warehouse (star schema)", step6_build_warehouse),
    ("Create analytics views", step7_create_analytics_views),
]


def main():
    total = len(STEPS)
    for i, (label, step_module) in enumerate(STEPS, start=1):
        print(f"\n=== Step {i}/{total}: {label} ===")
        step_module.run()
    print("\nPipeline finished. Your data is ready in the analytics schema.")


if __name__ == "__main__":
    main()
