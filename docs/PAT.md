deprecated! - todo delete
## 🔐 What’s a PAT (Personal Access Token)?
A **PAT** replaces your GitLab username and password when accessing repositories over HTTPS — especially in CI/CD pipelines or Docker containers.

- It's safer than using a username/password.
- Required if you use 2FA or access GitLab via scripts/containers.
- Used like:  
  `https://<username>:<PAT>@gitlab.example.com/group/project.git`

---

## 🧩 Why It Matters for Git Submodules
When your main repo (`client`) has a **submodule** (e.g., `connector_base`), cloning the main repo **also triggers a fetch** for the submodule.  
But unless that submodule is public or authenticated properly, you'll get errors like:

```
fatal: could not read Username for 'https://gitlab...': No such device or address
```

This happens **especially inside Docker containers**, where no interactive prompt is possible.

---

## ✅ How to Inject the PAT into the Submodule

### Step 1: Change the submodule URL to include your PAT
You inject the PAT for the **submodule repo**, not the main one. Run this inside your **cloned `client` repo**:

```bash
git submodule set-url connector_base https://<your_username>:<your_PAT>@gitlab.lrz.de/data-fabric/connector_base.git
```

### Step 2: Commit the `.gitmodules` update
This updates the submodule reference in `.gitmodules`:

```bash
git add .gitmodules
git commit -m "Inject PAT into submodule URL"
```

### Step 3: Sync the updated config
This tells Git to update the local `.git/config` with the new submodule URL:

```bash
git submodule sync
```

---

## 🔄 Optional: Do it from the start with `git clone`
You can also clone the whole repo including the PAT inline:

```bash
git clone --recurse-submodules https://<your_username>:<your_PAT>@gitlab.lrz.de/data-fabric/client.git
```

---

## 📌 Important Notes

- The PAT should have **read_repository** permission at minimum.
- Be cautious: a committed PAT in `.gitmodules` is **visible to everyone with repo access**.
- For sensitive environments, consider **injecting the PAT via CI variables or Docker secrets** instead of hardcoding.

---

Let me know if you want a **secure version using `git-credentials`** or secrets in Docker!