import sys
from request_helper import handle_request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <filename>")
        sys.exit(1)

    request_file = sys.argv[1]

    try:
        with open(request_file, "r") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                
                # Split into: [ACTION, TARGET, CONTENT]
                # maxsplit=2 ensures we only split on the first two spaces
                parts = line.split(" ", 2)
                
                # Default empty content if only 2 fields provided
                action = parts[0]
                target = parts[1] if len(parts) > 1 else ""
                content = parts[2] if len(parts) > 2 else ""

                if not target:
                    print(f"Line {line_num}: Missing target. Skipping.")
                    continue
                
                print(f"--- Request {line_num}: {action} | Target: {target} | Content: {content} ---")
                
                # Pass all three to the helper
                response = handle_request(action, target, content)
                print(f"Response: {response}\n")

    except FileNotFoundError:
        print(f"Error: Request file '{request_file}' not found.")