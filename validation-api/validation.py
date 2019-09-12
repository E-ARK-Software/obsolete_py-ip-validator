### Validation Methods
Method to validate packages in archive formate
ValidationResult validate(SpecificationDetails spec, InputStream packageStream);

Method to validate packages in a directory
ValidationResult validate(SpecificationDetails spec, Path packageRoot);



/**
 * The result of checking a rule against a package
 */
CheckResult {
  # True if the check passed, false otherwise
  boolean isPassed;

  # Location needs design. It should be the best way of reporting the source
  # of the failure to the user, e.g. the path, line number and xpath for a METS
  # file location. I figured you might be best figuring our what actually works
  # here...
  Location location;

  # A list of relative package paths to items related to test failure,
  # e.g. a missing package file, a file that fails hash integrity checking, etc.
  List<Path> relatedItems;
}

/**
 * Couples a rule with a list of results
 */
ValidationCheck {
  # The rule under test
  ValidationRule rule;

  # Set of results for the check. In practise will normally be pre-sorted into
  # pass and fails for use in report.
  Set<CheckResult> results;
}

/**
 * I'm a little woolly on this one. It needs To summarise the overall result of
 * validation. That in turn depends on the balance of INFO | WARN | ERROR check
 * results. A good starting point might be the most severe level encountered.
 */
ValidationResult {
  # Overall validation result level
  LEVEL level;

  # Overall package status following checks, WELLFORMED | VALID | COMPLETE
  STATUS status;

  # The number of validation checks passed
  int passedChecks;

  # The number of error level validation checks
  int errorTotal;

  # The number of warning level validation checks
  int warningTotal;

  # The number of info level validation checks
  int infoTotal;
}

/**
 * The result of package validation, this will need to be a little more sophisticated
 * around reporting of checks by rule LEVEL, e.g. ERRORS, WARNINGS and INFO
 * I'm not sure that these aren't better supported by convenience methods and
 * a Map structure in the implementation e.g. <LEVEL, List<ValidateCheck>>
 */
ValidationReport {
  # The details of the spec used for valdiation
  SpecificationDetails specDetails;

  # The package level result details
  ValidationResult result;

  # List of checks performed and passed, might be empty because of config
  # default should be to not record passedChecks to keep the resources use and
  # report size down. Good for testing and debugging though
  Set<ValidationCheck> passedChecks;

  # List of error level checks
  Set<ValidationCheck> errors;

  # List of warning level checks
  Set<ValidationCheck> warnings;

  # List of info level checks
  Set<ValidationCheck> infos;
}
```

### Software build details
Think about reporting build details (version, date) as a defined structure.
