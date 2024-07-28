# generate_zap_scan_steps_and_execute.py
import csv
import json
import subprocess
import os

steps = []

with open('Testdata/endpoint.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    print(f"CSV Headers: {headers}")
    if 'url' not in headers:
        raise KeyError("'url' column is missing from CSV file")

    for row in reader:
        url = row['url']
        steps.append({
            'name': f"ZAP Scan {url}",
            'uses': 'zaproxy/action-api-scan@v0.7.0',
            'with': {
                'token': '${{ secrets.GITHUB_TOKEN }}',
                'docker_name': 'ghcr.io/zaproxy/zaproxy:stable',
                'format': 'openapi',
                'target': url,
                'cmd_options': '-J /.zap/report_json.json -w /.zap/report_md.md -r /.zap/report_html.html -a'
            }
        })

# Save the steps to a JSON file (for debugging or future use)
with open('dynamic_steps.json', 'w') as f:
    json.dump(steps, f)

# Execute each step
for step in steps:
    name = step['name']
    uses = step['uses']
    token = step['with']['token']
    docker_name = step['with']['docker_name']
    format = step['with']['format']
    target = step['with']['target']
    cmd_options = step['with']['cmd_options']

    print(f"Running {name}")
    command = f"docker run --rm -v $(pwd):/.zap/wrk/:rw -t {docker_name} .zap-api-scan.py -t {target} -f {format} {cmd_options}"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"ZAP scan for {target} failed with exit code {e.returncode}")
        print("Output:", e.output)
        print("Error:", e.stderr)

    # Verify that the report files are created
    report_files = ["/.zap/report_json.json", "/.zap/report_md.md", "/.zap/report_html.html"]
    for report_file in report_files:
        if not os.path.exists(report_file):
            print(f"Report file {report_file} was not created.")
        else:
            print(f"Report file {report_file} exists.")
