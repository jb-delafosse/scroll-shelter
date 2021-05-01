# scroll-shelter

<div align="center">

[![Build status](https://github.com/scroll-shelter/scroll-shelter/workflows/build/badge.svg?branch=master&event=push)](https://github.com/scroll-shelter/scroll-shelter/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/scroll-shelter.svg)](https://pypi.org/project/scroll-shelter/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/scroll-shelter/scroll-shelter/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/scroll-shelter/scroll-shelter/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/scroll-shelter/scroll-shelter/releases)
[![License](https://img.shields.io/github/license/scroll-shelter/scroll-shelter)](https://github.com/scroll-shelter/scroll-shelter/blob/master/LICENSE)

`scroll-shelter` is an ongoing personal project where I try to build a platform that can handle and process handwritten notes.

**disclaimer:** currently it is just me fiddling around with concepts and trying libraries. It is very likely it won't end up anywhere 
</div>


## 🚀 Features

Nothing yet.

## 🛠️ Contributing

### Package Manager

All manipulations with dependencies are executed through Poetry. If you're new to it, look through [the documentation](https://python-poetry.org/docs/).

<details>
<summary>Notes about Poetry</summary>
<p>

Poetry's [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:

- `poetry add numpy`
- `poetry run pytest`
- `poetry build`
- etc

</p>
</details>

### Makefile usage

[`Makefile`](https://github.com/scroll-shelter/scroll-shelter/blob/master/Makefile) contains many functions for fast assembling and convenient work.

<details>
<summary>1. Download Poetry</summary>
<p>

```bash
make download-poetry
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

```bash
make install
```

If you do not want to install pre-commit hooks, run the command with the NO_PRE_COMMIT flag:

```bash
make install NO_PRE_COMMIT=1
```

</p>
</details>

<details>
<summary>3. Check the security of your code</summary>
<p>

```bash
make check-safety
```

This command launches a `Poetry` and `Pip` integrity check as well as identifies security issues with `Safety` and `Bandit`. By default, the build will not crash if any of the items fail. But you can set `STRICT=1` for the entire build, or you can configure strictness for each item separately.

```bash
make check-safety STRICT=1
```

or only for `safety`:

```bash
make check-safety SAFETY_STRICT=1
```

multiple

```bash
make check-safety PIP_STRICT=1 SAFETY_STRICT=1
```

> List of flags for `check-safety` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`.

</p>
</details>

<details>
<summary>4. Check the codestyle</summary>
<p>

The command is similar to `check-safety` but to check the code style, obviously. It uses `Black`, `Darglint`, `Isort`, and `Mypy` inside.

```bash
make check-style
```

It may also contain the `STRICT` flag.

```bash
make check-style STRICT=1
```

> List of flags for `check-style` (can be set to `1` or `0`): `STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.

</p>
</details>

<details>
<summary>5. Run all the codestyle formaters</summary>
<p>

Codestyle uses `pre-commit` hooks, so ensure you've run `make install` before.

```bash
make codestyle
```

</p>
</details>

<details>
<summary>6. Run tests</summary>
<p>

```bash
make test
```

</p>
</details>

<details>
<summary>7. Run all the linters</summary>
<p>

```bash
make lint
```

the same as:

```bash
make test && make check-safety && make check-style
```

> List of flags for `lint` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.

</p>
</details>

<details>
<summary>8. Build docker</summary>
<p>

```bash
make docker
```

which is equivalent to:

```bash
make docker VERSION=latest
```

More information [here](https://github.com/scroll-shelter/scroll-shelter/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup docker</summary>
<p>

```bash
make clean_docker
```

or to remove all build

```bash
make clean
```

More information [here](https://github.com/scroll-shelter/scroll-shelter/tree/master/docker).

</p>
</details>

## 🛡 License

[![License](https://img.shields.io/github/license/scroll-shelter/scroll-shelter)](https://github.com/scroll-shelter/scroll-shelter/blob/master/LICENSE)

This project is licensed under the terms of the `GNU GPL v3.0` license. See [LICENSE](https://github.com/scroll-shelter/scroll-shelter/blob/master/LICENSE) for more details.

## 📃 Citation

```
@misc{scroll-shelter,
  author = {scroll-shelter},
  title = {`scroll-shelter` is an ongoing personal project where I try to build a platform that can handle and process handwritten notes.},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/scroll-shelter/scroll-shelter}}
}
```

## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
