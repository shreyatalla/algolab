# Lesson 4: Git, GitHub & Going Live

**Goal:** save your work with Git, put it on GitHub, and publish the AlgoLab website with a public link.
**Time:** about 1.5–2 hours. Most of it is one-time setup.

This lesson has no coding exercises. Instead, each step ends with a ✅ check so you know it worked. By the end you'll have a GitHub repo and a live site you can put on your resume.

---

## 1. What are Git and GitHub?

- **Git** is a program on your computer that saves snapshots of your project, called **commits**. Each commit records exactly what changed and when, with a short message. You can always look back at, or go back to, an earlier snapshot.
- **GitHub** is a website that stores a copy of your Git project online, called a **repository** or **repo**. It's where employers can see your code.
- **Streamlit Community Cloud** is a free service that reads your repo on GitHub and runs `app.py` as a public website.

The flow looks like this:

```
your computer  ──git push──▶  GitHub  ──automatic──▶  your live site
```

## 2. The four commands you'll use every day

| Command | What it does |
|---|---|
| `git status` | Shows what's changed since your last commit. **Run it often**, it's always safe. |
| `git add <file>` | Chooses a file to include in the next commit ("staging"). `git add .` chooses everything that's changed. |
| `git commit -m "message"` | Saves the staged changes as a snapshot with your message. |
| `git push` | Uploads your new commits to GitHub. |

---

## 3. Tell Git who you are (one time only)

Every commit is labeled with a name and email, and **those are public on GitHub**. So before your first commit, set them:

```bash
cd ~/algolab
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

💡 **Privacy tip:** if you don't want your personal email visible on GitHub, you can use a private "noreply" address that GitHub gives you. You'll find it in step 5, under GitHub **Settings → Emails**. It looks like `12345678+username@users.noreply.github.com`. You can set up with your normal email now and switch later by re-running the `user.email` line.

✅ **Check:** `git config user.name` prints your name.

## 4. Your first commit

I already ran `git init` in this folder when I set up the project. That command turns a folder into a Git project, and you only ever run it once per project. So you can go straight to committing.

```bash
git status
```

You'll see a list of "untracked files" in red. Git sees them but isn't saving them yet.

Notice that `.venv/` and `__pycache__/` **aren't** in the list. That's because of the file `.gitignore`, which lists things Git should ignore. `.venv` is big, and anyone can rebuild it from `requirements.txt`, so it doesn't belong on GitHub.

Now stage everything and commit:

```bash
git add .
git status                  # the files are green now: they're staged
git commit -m "Set up AlgoLab and complete Lessons 1-3"
```

✅ **Check:** `git log --oneline` shows your commit.

### Writing good commit messages

Write the message as a short summary of **what the commit does**, as though finishing the sentence "This commit will…":
- ✅ `Add lesson 4 git guide`
- ✅ `Fix common_elements sorting bug`
- ❌ `stuff`, `update`, `asdfgh`

Recruiters sometimes scroll through commit history, and clear messages look professional.

## 5. Create your GitHub account and repo

1. Go to **github.com** and sign up (or sign in). Your username appears in your repo's link, so choose something professional, ideally your name.
2. Click the **+** in the top right → **New repository**.
3. Fill in:
   - **Repository name:** `algolab`
   - **Description:** `Data structures and interview problems built from scratch in Python, with a live Streamlit site`
   - **Public** (it has to be public for employers to see it, and for the free hosting)
   - ⚠️ **Don't** tick "Add a README", ".gitignore" or "license". You already have files, and GitHub adding its own would cause a conflict.
4. Click **Create repository**.

GitHub then shows a page of setup commands. Keep it open, since you need the repo's URL from it. It looks like `https://github.com/USERNAME/algolab.git`.

## 6. Connect your folder to GitHub and push

Back in the terminal. Replace `USERNAME` with your GitHub username:

```bash
git remote add origin https://github.com/USERNAME/algolab.git
git push -u origin main
```

- `git remote add origin ...` tells Git where your GitHub copy lives. `origin` is the standard nickname for it.
- `git push -u origin main` uploads your `main` branch. The `-u` means that from now on, a plain `git push` is enough.

### Signing in when you push

The first push asks for a **username** and **password**. GitHub doesn't accept your normal account password here. You need a **personal access token** instead, which is a password made only for Git:

1. On GitHub, click your profile picture → **Settings** → **Developer settings** (at the bottom of the left menu) → **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)**.
2. **Note:** `algolab laptop`. **Expiration:** 90 days is fine. **Scopes:** tick **`repo`**.
3. Click **Generate token** and **copy it now**. GitHub only shows it once.
4. Back in the terminal: username = your GitHub username, password = **paste the token**. (Nothing appears on screen as you paste. That's normal, just press Enter.)

Your Mac saves the token in its Keychain, so you won't be asked again. Treat the token like a password: don't paste it into your code or share it.

✅ **Check:** refresh your repo page on GitHub. Your files and README are there.

## 7. Deploy the site 🚀

1. Go to **share.streamlit.io** and click **Continue with GitHub**. Allow it to access your account.
2. Click **Create app** → **Deploy a public app from GitHub**.
3. Fill in:
   - **Repository:** `USERNAME/algolab`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL:** choose a name, for example `yourname-algolab`. That becomes `yourname-algolab.streamlit.app`.
   - Open **Advanced settings** and set **Python version** to **3.11**, to match the version on your computer.
4. Click **Deploy**.

The first build takes a few minutes, because it installs everything in `requirements.txt`. Then you'll see your home page.

✅ **Check:** open your site's link in a private browser window. If it loads there, anyone can see it.

(If a sleeping-app message ever appears, that's normal on the free plan: a site with no visitors for a while goes to sleep, and clicking the wake-up button starts it again.)

## 8. The everyday loop: change, commit, push

Now try the full cycle once. Open `README.md` and replace this line:

```
**Live site:** _coming in Lesson 4_
```

with your real link:

```
**Live site:** https://yourname-algolab.streamlit.app
```

Then:

```bash
git status                       # README.md shows as "modified"
git add README.md
git commit -m "Add live site link to README"
git push
```

✅ **Check:** your repo page on GitHub now shows the link on the front page.

**From now on, when you finish each lesson:**

```bash
git add .
git commit -m "Complete lesson N: <topic>"
git push
```

Every push also updates your live site automatically within a minute or two. Try it: change the text in `app.py`, push, and refresh your site.

---

## 🆘 If something goes wrong

| Message | What it means / what to do |
|---|---|
| `Author identity unknown` | You skipped step 3. Set your name and email, then commit again. |
| `remote origin already exists` | You already ran `git remote add`. Fix the URL with `git remote set-url origin https://github.com/USERNAME/algolab.git` |
| `Authentication failed` / `Support for password authentication was removed` | You entered your GitHub password instead of the token. Make a token (step 6) and use it as the password. |
| `rejected ... fetch first` | GitHub has changes you don't have, usually because a README was added on the website. Ask me and I'll walk you through it. |
| The site shows `ModuleNotFoundError` | A library is missing from `requirements.txt`. |

For anything else, paste the whole error message here.

## 🎤 Interview corner

Git questions come up in interviews, especially "tell me about your workflow". Know these in one sentence each:
- **Commit:** a saved snapshot of the project, with a message saying what changed.
- **Branch:** a separate line of work, so you can try something without breaking `main`.
- **Pull request (PR):** asking for a branch's changes to be reviewed and merged into `main`. It's how teams review each other's code.
- **Merge conflict:** two changes edited the same lines, and Git needs a person to choose which to keep.

You'll also be able to say "my project is deployed automatically: every push to `main` updates the live site". That's called **continuous deployment**, and it's a good thing to mention.
