# Raw-Dvc - Other

**Pages:** 2

---

## Contributing to the Documentation

**URL:** https://doc.dvc.org/contributing/docs

**Contents:**
- Contributing to the Documentation
- Structure of the project
- Submitting changes
- Development environment
  - All commands
  - ENV variables
- Doc style guidelines (JavaScript and Markdown)
- General language guidelines
      - Content
- Product

We welcome any contributions to our documentation repository, dvc.org. Contributions can be updates to the documentation content, or (rare) changes to the JS engine we use to run the website.

In case of a minor change, you can use the Edit on GitHub button to open the source code page. Use the Edit button (pencil icon) to edit the file in-place, and then Commit changes from the bottom of the page.

To contribute documentation, these are the relevant locations:

Merging the appropriate changes to these files into the main branch is enough to update the docs and redeploy the website.

Find or open a new issue in the issue tracker to let us know that you are working on this.

Format the source code by following the style guidelines below. We highly recommend setting up a development environment as explained below. Among other things, it can help format the documentation and JS code automatically.

Push the changes to your fork of dvc.org and submit a PR to the upstream repo.

We will review your PR as soon as possible. Thank you for contributing!

We highly recommend running this web app locally to check documentation changes before submitting them, and it's quite necessary when making changes to the website engine itself. Source code and content files need to be properly formatted and linted as well, which is also ensured by the full setup below.

Make sure you have a recent LTS version of Node.js (>=18.0.0, <=20.x), and install Yarn:

In Windows, you may need to install Visual Studio Build Tools, and the [Windows

Having cloned this project locally, navigate into the directory and install the project dependencies with Yarn:

Launch the server locally with:

This will start the server on the default port, 8000. Visit http://localhost:8000/ and navigate to the page in question. This will also enable the pre-commit Git hook that will be formatting and linting your code and documentation files automatically.

These Node scripts are specified in the docs repo's package.json file.

To build the project and run it:

All the tests, formatting, and linters below will be automatically enforced before every commit with Husky and lint-staged before each commit, as well as with GitHub Actions upon submitting PRs.

If you change source code files, run tests:

We use Prettier to format our source code. Below is a set of wrapper commands for your convenience:

We use linters (e.g. ESLint) to check source code style and detect different errors:

To use the fix variant of all of these tools in one command, use yarn fix-all.

Note that you can always use the formatter or linter directly (e.g. yarn eslint <file> or yarn prettier --check <file>).

Some environment variables are required to deploy this project to production, others can be used to debug the project. Please check the production system settings to see all the variables that production and deployment system depend on.

Some available variables:

Some of the following rules are applied automatically by a pre-commit Git hook that is installed when yarn runs (see dev env).

No trailing white spaces are allowed.

Text content must be properly formatted at 80 symbols width.

💡 We recommend using Visual Studio Code with the Rewrap plugin for help with this.

You can see the configuration of our formatter tool (Prettier) here. You may also run the formatting commands manually. (Advanced usage of Prettier is available through yarn prettier ...)

Markdown: Using dvc <command>, the docs engine will create a link to that command automatically. (No need to use []() explicitly to create them.)

Markdown: Using dvc.api.<api_method>() or dvc.api, the docs engine will create a link to that API method automatically. (No need to use []() explicitly to create them.)

Markdown: Bullet lists shouldn't be too long (5-7 items max., ideally).

Markdown: The text in each bullet item also shouldn't be too long (3 sentence paragraphs max.) Full sentence bullets should begin with a capital letter and end in period .. Otherwise, they can be all lower case and have no ending punctuation. Bullets can be separated by an empty line if they contain several paragraphs, but this is discouraged: try to keep items short.

Markdown: Syntax highlighting in fenced code blocks should use the usage dvc, dvctable, yaml, or diff custom languages.

Check out the .md source code of any command reference to get a better idea, for example in this very file.

We try to use a casual and fun tone in our docs. We also avoid authoritative language such as "As you can see, clearly this is what happened, of course" etc. which while good-intentioned, may scare readers off.

We prefer general, human-friendly language rather than exact jargon as long as it's correct. Example: avoid Git jargon such as revision or reference, preferring the more basic terms commit or version.

The command reference contains some of our most technical documents where specialized language is used the most, but even there, we use expandable sections for complex implementation details.

Start by writing the essence in simple terms, and complete it with clarifications, edge cases, or other precisions in a separate iteration.

We use bold text for emphasis, and italics for special terms.

We also use "emoji" symbols sparingly for visibility on certain notes. Mainly:

Some other emojis currently in use here and there: ⚡ ✅ 🙏 🐛 ⭐ ⚙️ ℹ️ (among others).

🐛 Found an issue? Let us know! Or fix it:

❓ Have a question? Join our chat, we will help you:

**Examples:**

Example 1 (unknown):
```unknown
$ npm install -g yarn
```

Example 2 (unknown):
```unknown
$ yarn develop
```

---

## DVC Documentation

**URL:** https://doc.dvc.org

**Contents:**
- DVC Documentation
  - Get Started
  - User Guide
  - Use Cases
- Product
- Help
- Community
- Legal

DVC can be installed on Visual Studio Code, any system terminal, and used as a Python library.

✅ If you have any questions or need specific help, feel free to join our community or use the support channels. We are very responsive⚡.

✅ Check out our GitHub repositories: DVC give us a ⭐ if you like the project!

✅ Contribute to DVC on GitHub or help us improve this documentation 🙏.

🐛 Found an issue? Let us know! Or fix it:

❓ Have a question? Join our chat, we will help you:

---
