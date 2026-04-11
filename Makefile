# Makefile для управления RULE

RULES_DIR = pack/rules
SCRIPTS_DIR = scripts
TEMPLATE = $(RULES_DIR)/RULE-TEMPLATE.md

.PHONY: help validate validate-all generate

help:
	@echo "Available targets:"
	@echo "  make validate RULE=RULE-001    - Validate specific RULE"
	@echo "  make validate-all              - Validate all RULEs"
	@echo "  make generate NAME=...         - Generate new RULE"
	@echo "  make list                      - List all RULEs"

validate:
	@if [ -z "$(RULE)" ]; then \
		echo "Usage: make validate RULE=RULE-001"; \
		exit 1; \
	fi
	python3 $(SCRIPTS_DIR)/rule-validator.py $(RULES_DIR)/$(RULE)*.md

validate-all:
	python3 $(SCRIPTS_DIR)/rule-validator.py --all --dir $(RULES_DIR)

generate:
	@if [ -z "$(NAME)" ] || [ -z "$(CATEGORY)" ]; then \
		echo "Usage: make generate NAME=mastitis-detection CATEGORY=infectious"; \
		echo "Categories: metabolic, reproductive, infectious, nutritional, management"; \
		exit 1; \
	fi
	python3 $(SCRIPTS_DIR)/rule-generator.py --name $(NAME) --category $(CATEGORY)

list:
	@echo "Available RULEs:"
	@ls -1 $(RULES_DIR)/RULE-*.md 2>/dev/null | grep -v TEMPLATE | xargs -I {} basename {} | sed 's/^/  - /'
