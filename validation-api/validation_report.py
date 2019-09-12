# The result of package validation, this will need to be a little more sophisticated
# around reporting of checks by rule LEVEL, e.g. ERRORS, WARNINGS and INFO
# I'm not sure that these aren't better supported by convenience methods and
# a Map structure in the implementation e.g. <LEVEL, List<ValidateCheck>>

import validation
import specification

class ValidationReport:

    # The details of the spec used for valdiation
    SpecificationDetails spec_details;

    # The package level result details
    ValidationResult result;

    # List of checks performed and passed, might be empty because of config
    # default should be to not record passedChecks to keep the resources use and
    # report size down. Good for testing and debugging though
    Set<ValidationCheck> passed_checks;

    # List of error level checks
    Set<ValidationCheck> errors;

    # List of warning level checks
    Set<ValidationCheck> warnings;

    # List of info level checks
    Set<ValidationCheck> infos;
