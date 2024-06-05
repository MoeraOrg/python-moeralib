import jsonschema


def add_pruning_to_validator(validator_class):
    validate_properties = validator_class.VALIDATORS["properties"]

    def remove_additional_properties(validator, properties, instance, schema):
        for prop in list(instance.keys()):
            if prop not in properties:
                del instance[prop]

        for error in validate_properties(validator, properties, instance, schema,):
            yield error

    return jsonschema.validators.extend(validator_class, {"properties" : remove_additional_properties})


PruningValidator = add_pruning_to_validator(jsonschema.validators.Draft7Validator)


def validate(instance, schema):
    return PruningValidator(schema).validate(instance)
