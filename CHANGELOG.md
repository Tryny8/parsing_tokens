# Changelog

All notable changes to this project will be documented in this file.


## [0.3.0] - 2026-01-04

### Breaking Changes
- `compile_multiples_tokens_matcher` no longer uses hardcoded patterns.
  It now requires a list of pattern dictionaries.
- `TokenParser` internal logic has been refactored to support dynamic
  multi-pattern compilation.
- Previous usage relying on implicit hardcoded token patterns must be updated.

### Added
- Dynamic multi-pattern compilation via `compile_multiples_tokens_matcher(list_patterns)`
- Validation of pattern dictionaries using `_is_valid_dict_pattern`
- Centralized pattern key registry (`KEYS_PATTERN`)
- Support for multiple active token definitions in `TokenParser`
- New methods:
  - `reset_balise`
  - `get_all_balises`

### Changed
- Token parsing is now fully data-driven (dictionary-based)
- `TokenParser` supports both single-pattern and multi-pattern modes
- Improved separation between pattern definition and compilation

### Internal
- Refactored parser architecture to prepare future extensibility
- Improved validation and error messages for invalid pattern definitions

### Tests
- Added unit tests covering multi-pattern compilation and validation


## [0.2.1] - 2026-01-04
### Fix
- Adding function [0.2.0] in __init__.py for visibility API

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