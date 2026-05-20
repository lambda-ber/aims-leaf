RUN = uv run
SCHEMA := src/aims_leaf_schema/schema/aims_leaf_ber_schema.yaml
SCHEMA_SOURCES := $(wildcard src/aims_leaf_schema/schema/*.yaml)
DOCDIR := ./docs
ELEMENTSDIR := ./docs/elements
PYDANTIC := src/aims_leaf_schema/pydantic.py

all: gen-project gendoc test-examples gen-pydantic gen-sssom
test: gen-project

gen-project:
	$(RUN) gen-project --config-file config.yaml $(SCHEMA) -d assets

gen-pydantic: $(PYDANTIC)

$(PYDANTIC): $(SCHEMA_SOURCES)
	$(RUN) gen-pydantic $(SCHEMA) > $(PYDANTIC)

# Generate schema documentation to docs/elements/ and copy manual docs
gendoc: $(DOCDIR)
	cp -pr src/docs/* $(DOCDIR)
	$(RUN) gen-doc -d $(ELEMENTSDIR) $(SCHEMA)

gen-sssom: assets/sssom/aims_leaf_ber_schema.sssom.tsv

assets/sssom/aims_leaf_ber_schema.sssom.tsv: $(SCHEMA_SOURCES)
	mkdir -p assets/sssom
	$(RUN) gen-sssom $(SCHEMA) -o $@

serve:
	$(RUN) mkdocs serve
