# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
### Added
- Token registry system (custom token types, balises, separators)

### Changed
- Validation logic now uses registries instead of hard-coded values

### Deprecated
- Hard-coded token type validation functions

---

## [0.2.0] - 2026-01-04
### Added
- Public API to register custom token types
- New `set_register_token_type()` function API
- New `set_register_balise()` function API
- New `set_register_separator()` function API
- New `get_register_all_token_type()` function API
- New `get_register_all_balise()` function API
- New `get_register_all_separator()` function API

- New `add_token_type()` method TokenParser
- New `add_balise()` method TokenParser
- New `add_separator()` method TokenParser
- New `get_all_token_type()` method TokenParser
- New `get_all_balise()` method TokenParser
- New `get_all_separator()` method TokenParser

### Changed
- Token / balise / separator validation logic is now extensible

---

## [0.1.0] - 2026-01-03
### Added
- Initial token parsing engine