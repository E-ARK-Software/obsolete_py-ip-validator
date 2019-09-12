# I'm a little woolly on this one. It needs To summarise the overall result of
# validation. That in turn depends on the balance of INFO | WARN | ERROR check
# results. A good starting point might be the most severe level encountered.

import level
import status

class ValidationResult:

    # Overall validation result level
    LEVEL level;

    # Overall package status following checks, WELLFORMED | VALID | COMPLETE
    STATUS status;

    # The number of validation checks passed
    int passed_checks;

    # The number of error level validation checks
    int error_total;

    # The number of warning level validation checks
    int warning_total;

    # The number of info level validation checks
    int info_total;

    def describe(self):
        print("Validation result:", "level", level, "status", status, "passed checks", passed_checks, "error total", error_total, "warning total", warning_total, "info total", info_total)
