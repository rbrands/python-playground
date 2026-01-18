# Branch Protection and Pull Request Setup

This document explains how to configure repository settings to make Pull Requests (PRs) mandatory and ensure only the repository owner can perform reviews.

## Overview

The following settings ensure:
1. ✅ All changes must be made via Pull Requests
2. ✅ Direct pushes to the `main` branch are not allowed
3. ✅ Only @rbrands can review and approve Pull Requests
4. ✅ An approved review is required before merging

## CODEOWNERS File

The `.github/CODEOWNERS` file has been created. It defines @rbrands as the code owner for all files in the repository.

## Setting Up GitHub Branch Protection Rules

### Step 1: Open Repository Settings
1. Go to https://github.com/rbrands/python-playground
2. Click on **Settings**
3. Select **Branches** from the left menu

### Step 2: Add Branch Protection Rule
1. Click on **Add branch protection rule** (or "Add rule")
2. In "Branch name pattern" enter: `main`

### Step 3: Enable the Following Options

#### Require a pull request before merging
- ✅ **Require a pull request before merging**
  - ✅ **Require approvals**: Set to at least 1 approval
  - ✅ **Dismiss stale pull request approvals when new commits are pushed** (optional but recommended)
  - ✅ **Require review from Code Owners** - **IMPORTANT!** This ensures only @rbrands can review

#### Additional Recommended Settings
- ✅ **Require status checks to pass before merging** (optional, if you use CI/CD)
- ✅ **Require branches to be up to date before merging** (recommended)
- ✅ **Do not allow bypassing the above settings** - **IMPORTANT!** This prevents bypassing the rules

#### Restrictions (Optional but recommended)
- ✅ **Restrict who can push to matching branches**
  - Add only @rbrands or leave empty for maximum security
  - This prevents others from pushing directly

### Step 4: Save
1. Scroll down and click **Create** or **Save changes**

## Workflow After Setup

### For Contributors:
1. Create a fork of the repository or create a new branch
2. Make changes in the branch
3. Open a Pull Request
4. Wait for review and approval from @rbrands
5. After approval, the PR can be merged

### For @rbrands (Owner):
1. Review Pull Requests
2. Request changes if needed
3. Approve after successful review
4. Merge the Pull Request

## Verification

After setup, you can test if the settings work:

1. Try to push directly to the `main` branch - this should be blocked
2. Create a test branch and a Pull Request
3. The PR should show status "Review required from @rbrands"
4. The merge button should only be enabled after your approval

## Additional Information

- **CODEOWNERS**: This file in `.github/CODEOWNERS` automatically defines required reviewers
- **Branch Protection**: Configured in GitHub Settings → Branches
- **Documentation**: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches

## Important Notes

⚠️ **Note**: Branch Protection Rules can only be configured through the GitHub web interface or GitHub API, not through repository files.

✅ **Advantage**: The CODEOWNERS file is versioned and part of the repository, so reviewer assignment happens automatically.

🔒 **Security**: With "Do not allow bypassing the above settings" even the repository owner cannot bypass the rules (recommended for maximum code quality).
