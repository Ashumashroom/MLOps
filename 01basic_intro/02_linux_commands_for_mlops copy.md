
# Linux Commands Cheat Sheet for MLOps

This is a comprehensive list of useful Linux commands for MLOps practitioners.

## 📁 File and Directory Commands
- `ls -al` — List all files including hidden in long format
- `cd <dir>` — Change directory
- `pwd` — Print working directory
- `mkdir <dir>` — Create a new directory
- `rm <file>` — Remove a file
- `rm -r <dir>` — Remove a directory and its contents
- `cp <src> <dest>` — Copy files or directories
- `mv <src> <dest>` — Move or rename files/directories

## 📄 File Viewing and Editing
- `cat <file>` — View file content
- `less <file>` — View file with scroll
- `head <file>` — View the first 10 lines
- `tail <file>` — View the last 10 lines
- `nano <file>` — Edit file in terminal
- `vim <file>` — Advanced terminal-based text editor

## 🔍 Search and Find
- `find <dir> -name <pattern>` — Search files by name
- `grep <pattern> <file>` — Search pattern in a file
- `grep -r <pattern> <dir>` — Recursive grep in directories

## 📦 Package Management
- `apt update` — Update package list (Debian/Ubuntu)
- `apt install <pkg>` — Install package
- `pip install <pkg>` — Install Python package
- `conda install <pkg>` — Install package using conda

## 🧠 Process and System Monitoring
- `top` — Live view of processes
- `htop` — Enhanced top (if installed)
- `ps aux` — List all running processes
- `kill <pid>` — Kill process by PID

## 🔐 Permissions and Users
- `chmod <perm> <file>` — Change file permissions
- `chown <user>:<group> <file>` — Change file ownership
- `sudo <command>` — Run command as superuser

## 🌐 Networking
- `ping <host>` — Check network connectivity
- `curl <url>` — Fetch web resources
- `wget <url>` — Download from URL
- `ifconfig` or `ip a` — Show IP info
- `netstat -tulpn` — Show listening ports and processes

## 📂 Disk and Storage
- `df -h` — Show disk usage in human-readable form
- `du -sh <dir>` — Show disk usage of a directory
- `mount` / `umount` — Mount or unmount storage devices

## 🐳 Docker (for MLOps)
- `docker ps` — List running containers
- `docker images` — List downloaded images
- `docker run <image>` — Run container from image
- `docker exec -it <container> bash` — Access container shell

## ☁️ Kubernetes (Basic)
- `kubectl get pods` — List all pods
- `kubectl logs <pod>` — Get logs of a pod
- `kubectl exec -it <pod> -- bash` — Access pod shell

## 📌 Useful Shortcuts
- `Ctrl + C` — Terminate current command
- `Ctrl + Z` — Suspend current command
- `Ctrl + D` — Logout or end input
- `!!` — Repeat last command
- `history` — Show command history

---

✅ **Tip:** You can always use `man <command>` for the manual page of any command.
