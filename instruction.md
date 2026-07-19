There is an Apache-style access log located at `/app/access.log`. Analyze the network traffic contained within this log file and generate a structured summary report.

### Success Criteria
1. Parse every log entry to calculate:
   - The total number of request lines.
   - The count of unique client IP addresses.
   - The most frequently requested URL path.
2. Save your summary output as a valid JSON file exactly at `/app/report.json`.
3. The JSON file must strictly follow this key-value schema:
   ```json
   {
     "total_requests": <int>,
     "unique_ips": <int>,
     "top_path": "<string>"
   }