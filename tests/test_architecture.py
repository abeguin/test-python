"""
Tests for the project architecture.
"""

from pathlib import Path

import pytest
from pytestarch import EvaluableArchitecture, Rule, get_evaluable_architecture


@pytest.fixture
def project_root(request: pytest.FixtureRequest) -> Path:
    return request.config.rootpath


@pytest.fixture
def project_arch(project_root: Path) -> EvaluableArchitecture:
    code_root = project_root.joinpath("src/sfy_python_template")
    return get_evaluable_architecture(
        root_path=str(code_root), module_path=str(code_root)
    )


def package_a_and_package_b_are_indenpendant(project_arch: EvaluableArchitecture):
    print(project_arch)
    a = "sfy_python_template.package_a"
    b = "sfy_python_template.package_b"
    rule_fd = (
        Rule()
        .modules_that()
        .are_named(a)
        .should_not()
        .import_modules_that()
        .are_named(b)
    )
    rule_df = (
        Rule()
        .modules_that()
        .are_named(b)
        .should_not()
        .import_modules_that()
        .are_named(a)
    )
    rule_fd.assert_applies(project_arch)
    rule_df.assert_applies(project_arch)
