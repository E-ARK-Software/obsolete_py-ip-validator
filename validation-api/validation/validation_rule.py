# An individual validation rule, used to perform a "check", a Specification
# effectively comprises of sets of these.
import level

class ValidationRule:

    # The ID of the validation rule, e.g CSIP7
    String id;

    # An Enum type, one of ERROR | WARN | INFO
    LEVEL level;

    # The message given for the rule in a Validation Report
    String message;

    # A more detailed text description of the rule
    String description;

    def get_level(self, level):
        for l in levels:
            if l == level:
                return l

    def describe(self):
        print("Validation rule", id, level, message, description)
