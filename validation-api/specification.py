### Support for multiple validators
Do we want to support multiple specification and validators, e.g. AIP, SIP, or
multiple versions from a single endpoint?
This means supporting concepts such as specification details
e.g name, URL, version, etc. but we'll need those for reporting.

Set<Specification> supportedSpecifications();
Set<SpecificationDetails> supportedSpecificationSummaries();
Specification getSpecification(String specName, String specVersion);
boolean isSupported(String specName, String specVersion);


/**
 * The main details of a specification that can be used for conformance checking.
 */
SpecificationDetails {
  # Name and Version can be combined to make a unique key for multi specification
  # A unique name for the specification, e.g. E-ARK CSIP
  String name;

  # The version of the specification. In time, We may want a more sophisticated
  # structure behind version, e.g. int major, int minor, int patchNo, String qualifier
  # so we can easily make comparisons.
  String version;

  # A URL for the specification site or location
  URL location;

  # A more detailed textual description of the specification
  String description;
}

/**
 * The full specification, including rules.
 */
Specification {
  # The spec details
  SpecificationDetails details;

  # The set of validation rules associated with the specification
  Set<ValidationRule> rules;
}
