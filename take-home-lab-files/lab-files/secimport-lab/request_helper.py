import socket
import time
import os

# Helper to handle file read requests
def handle_request(action: str, target: str, content: str = ""):

    # READ Command
    if action == "READ":
        if content != "":
            return "ERROR: TOO MANY ARGUMENTS"
        try:
            with open(target, "r") as f:
                content = f.read()
    
        except Exception:
            return "ERROR: FILE NOT FOUND"
        
    # EXISTS Command
    elif action == "EXISTS":
        if content != "":
            return "ERROR: TOO MANY ARGUMENTS"
        if os.path.exists(target):
            return f"SUCCESS: {target} exists."
        return "ERROR: FILE NOT FOUND"
    
    # RENAME Command
    elif action == "RENAME":
        try:
            old_path = target
            new_path = content
            os.rename(old_path, new_path)
            return f"SUCCESS: Moved {old_path} to {new_path}"
        except Exception as e:
            return f"RENAME FAILED: {e}"

    # DELETE Command
    elif action == "DELETE":
        if content != "":
            return "ERROR: TOO MANY ARGUMENTS"
        try:
            os.remove(target)
            return f"SUCCESS: Deleted {target}"
        except Exception as e:
            return f"DELETE FAILED: {e}"
    
    # WRITE Command
    elif action == "WRITE":
        with open(target, "w") as f:
            f.write(content)
        return f"SUCCESS: Wrote \"{content}\" to {target}"
    
    # CONNECT Command
    elif action == "CONNECT":
        if content != "":
            return "ERROR: TOO MANY ARGUMENTS"
        try:
            host, port = target.split(":")
            port = int(port)
            
            # Actual connection isn't necessary for this lab. Simply pretend like connection was made.
            return f"SUCCESS: Connected to {host} on port {port}"
        except Exception as e:
            return f"CONNECTION FAILED: {e}"

    
    print("APPLICATION FINISHED")
    return content