import time
import random
import logging
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ==========================================
# 1. THE "BRAIN" (Train the AI Model)
# ==========================================
print("🧠 Training AI Model on common server errors...")

# Training Data: Real-world error logs mapped to "Actions"
# Format: (Log Message, Remediation Action)
data = [
    ("Connection refused by port 80", "RESTART_WEBSERVER"),
    ("httpd service is down", "RESTART_WEBSERVER"),
    ("Nginx 502 Bad Gateway", "RESTART_WEBSERVER"),
    ("Out of memory: Kill process 123", "CLEAR_CACHE"),
    ("System memory usage at 99%", "CLEAR_CACHE"),
    ("Disk quota exceeded in /var/log", "CLEAN_LOGS"),
    ("No space left on device", "CLEAN_LOGS"),
    ("Database lock wait timeout exceeded", "RESTART_DB"),
    ("Deadlock found when trying to get lock", "RESTART_DB"),
]

# Split data into inputs (X) and labels (y)
X_train = [row[0] for row in data]
y_train = [row[1] for row in data]

# Create a Pipeline: Convert Text to Numbers -> Train Naive Bayes Classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

print(f"✅ AI Model Trained! Accuracy: {model.score(X_train, y_train)*100:.2f}%")
print("------------------------------------------------")

# ==========================================
# 2. THE "DOCTOR" (Remediation Logic)
# ==========================================
def perform_fix(action, log_line):
    print(f"\n🔴 CRITICAL ERROR DETECTED: '{log_line.strip()}'")
    print(f"🤖 AI PREDICTION: Issue requires -> {action}")
    
    # Simulate taking action
    time.sleep(1) 
    if action == "RESTART_WEBSERVER":
        print(f"🛠️  EXEC: sudo systemctl restart nginx... [SUCCESS]")
    elif action == "CLEAR_CACHE":
        print(f"🧹 EXEC: redis-cli flushall... [SUCCESS]")
    elif action == "CLEAN_LOGS":
        print(f"🗑️  EXEC: rm -rf /var/log/*.old... [SUCCESS]")
    elif action == "RESTART_DB":
        print(f"🗄️  EXEC: sudo systemctl restart postgresql... [SUCCESS]")
    
    print("✅ SYSTEM STABILIZED.\n")

# ==========================================
# 3. THE "WATCHDOG" (Log Monitor)
# ==========================================
class LogHandler(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')
        # Go to the end of the file immediately
        self.file.seek(0, 2)

    def on_modified(self, event):
        if event.src_path == self.filename:
            # Read new lines
            new_lines = self.file.readlines()
            for line in new_lines:
                # Use AI to predict what to do
                if "error" in line.lower() or "failed" in line.lower() or "critical" in line.lower():
                    prediction = model.predict([line])[0]
                    perform_fix(prediction, line)

# ==========================================
# 4. SIMULATION (The "Chaos" Generator)
# ==========================================
if __name__ == "__main__":
    log_file = r"C:\Users\ma\Desktop\Python Code\server_logs.txt"
    
    # Create the file if it doesn't exist
    with open(log_file, 'w') as f:
        f.write("Server started...\n")

    # Start the Watchdog
    observer = Observer()
    observer.schedule(LogHandler(log_file), path='.', recursive=False)
    observer.start()

    print(f"👀 Watching {log_file} for chaos... (Press Ctrl+C to stop)")
    
    try:
        # Simulate a server environment running
        error_scenarios = [
            "CRITICAL: Out of memory: Kill process 5050 (java)",
            "ERROR: Connection refused by port 80",
            "WARNING: Disk quota exceeded in /var/log",
            "ERROR: Deadlock found when trying to get lock; try restarting transaction"
        ]

        while True:
            time.sleep(3) # Wait a bit
            
            # Randomly inject an error every few seconds
            if random.random() > 0.7: 
                error = random.choice(error_scenarios)
                with open(log_file, "a") as f:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"[{timestamp}] {error}\n")
            else:
                # Log normal behavior
                with open(log_file, "a") as f:
                    f.write(f"[{time.strftime('%H:%M:%S')}] INFO: Health check passed.\n")

    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Stopping Auto-Healer.")
    
    observer.join()