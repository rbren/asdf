# Template Customization Guide

To customize this template with your own app name, replace "asdf" and "asdf" throughout the codebase.

## One-liner to replace everything:

```bash
find . -type f \( -name "*.json" -o -name "*.toml" -o -name "*.md" -o -name "*.yml" -o -name "*.yaml" -o -name "*.sh" -o -name "*.jsx" -o -name "*.js" -o -name "*.py" -o -name "*.html" \) -not -path "./node_modules/*" -not -path "./.git/*" -not -name "TEMPLATE.md" -exec sed -i 's/asdf/YOUR-APP-NAME/g; s/asdf/Your App Name/g' {} \;
```

Replace `YOUR-APP-NAME` with your kebab-case app name and `Your App Name` with your title-case app name.

After running the command:
1. Run `npm install` to regenerate package-lock.json
2. Update any remaining specific references (like GitHub URLs, email domains, etc.)
3. Test your application with `npm run build`