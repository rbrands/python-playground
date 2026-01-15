# Branch Protection und Pull Request Setup

Dieses Dokument erklärt, wie die Repository-Einstellungen konfiguriert werden müssen, damit Pull Requests (PRs) verpflichtend sind und nur der Repository-Owner Reviews durchführen kann.

## Übersicht

Mit den folgenden Einstellungen wird sichergestellt:
1. ✅ Alle Änderungen müssen über Pull Requests erfolgen
2. ✅ Direktes Pushen zum `main` Branch ist nicht erlaubt
3. ✅ Nur @rbrands kann Pull Requests reviewen und approven
4. ✅ Ein genehmigtes Review ist erforderlich vor dem Merge

## CODEOWNERS Datei

Die Datei `.github/CODEOWNERS` wurde bereits erstellt. Sie definiert @rbrands als Code Owner für alle Dateien im Repository.

## GitHub Branch Protection Rules einrichten

### Schritt 1: Repository Settings öffnen
1. Gehe zu https://github.com/rbrands/python-playground
2. Klicke auf **Settings** (Einstellungen)
3. Wähle im linken Menü **Branches** aus

### Schritt 2: Branch Protection Rule hinzufügen
1. Klicke auf **Add branch protection rule** (oder "Add rule")
2. Bei "Branch name pattern" eingeben: `main`

### Schritt 3: Folgende Optionen aktivieren

#### Require a pull request before merging
- ✅ **Require a pull request before merging**
  - ✅ **Require approvals**: Setze auf mindestens 1 Approval
  - ✅ **Dismiss stale pull request approvals when new commits are pushed** (optional, aber empfohlen)
  - ✅ **Require review from Code Owners** - **WICHTIG!** Dies stellt sicher, dass nur @rbrands reviewen kann

#### Weitere empfohlene Einstellungen
- ✅ **Require status checks to pass before merging** (optional, falls du CI/CD verwendest)
- ✅ **Require branches to be up to date before merging** (empfohlen)
- ✅ **Do not allow bypassing the above settings** - **WICHTIG!** Dies verhindert, dass die Regeln umgangen werden

#### Einschränkungen (Optional aber empfohlen)
- ✅ **Restrict who can push to matching branches**
  - Füge nur @rbrands hinzu oder lasse es leer für maximale Sicherheit
  - Dies verhindert, dass andere direkt pushen können

### Schritt 4: Speichern
1. Scrolle nach unten und klicke auf **Create** oder **Save changes**

## Workflow nach der Einrichtung

### Für Contributors:
1. Fork des Repositories erstellen oder einen neuen Branch erstellen
2. Änderungen im Branch vornehmen
3. Pull Request öffnen
4. Warten auf Review und Approval von @rbrands
5. Nach Approval kann der PR gemergt werden

### Für @rbrands (Owner):
1. Pull Requests reviewen
2. Bei Bedarf Änderungen anfordern
3. Nach erfolgreichem Review approven
4. Pull Request mergen

## Verifizierung

Nach der Einrichtung kannst du testen, ob die Einstellungen funktionieren:

1. Versuche direkt zum `main` Branch zu pushen - dies sollte blockiert werden
2. Erstelle einen Test-Branch und einen Pull Request
3. Der PR sollte den Status "Review required from @rbrands" anzeigen
4. Nur nach deinem Approval sollte der Merge-Button aktiviert werden

## Zusätzliche Informationen

- **CODEOWNERS**: Diese Datei in `.github/CODEOWNERS` definiert automatisch Required Reviewers
- **Branch Protection**: Wird in GitHub Settings → Branches konfiguriert
- **Dokumentation**: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches

## Wichtige Hinweise

⚠️ **Hinweis**: Branch Protection Rules können nur über die GitHub Web-Oberfläche oder die GitHub API konfiguriert werden, nicht durch Dateien im Repository.

✅ **Vorteil**: Die CODEOWNERS-Datei ist versioniert und Teil des Repositories, so dass die Reviewer-Zuweisung automatisch erfolgt.

🔒 **Sicherheit**: Mit "Do not allow bypassing the above settings" kann auch der Repository-Owner die Regeln nicht umgehen (empfohlen für maximale Code-Qualität).
