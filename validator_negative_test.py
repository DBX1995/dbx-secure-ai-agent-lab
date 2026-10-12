from validated_grounded_analyzer import validate_result


unsupported_result = {
    "primary_technical_capabilities": [
        {
            "finding": "AWS security engineering",
            "evidence": [
                "Required support includes: AWS security engineering"
            ]
        }
    ],
    "roles_requested": [
        {
            "role": "Cloud Security Engineer",
            "evidence": [
                "The agency expects to require: 1 Cloud Security Engineer"
            ]
        }
    ],
    "clearance_requirement": {
        "finding": "Secret clearance preferred",
        "evidence": [
            "Security requirement: Secret clearance preferred"
        ]
    },
    "dbx_alignment": {
        "finding": "This opportunity is a strong fit for DBX Solutions.",
        "evidence": []
    }
}

errors = validate_result(
    result=unsupported_result,
    dbx_profile=None
)

if errors:
    print("NEGATIVE TEST PASSED")
    print("Validator correctly rejected unsupported output.")

    for error in errors:
        print(f"- {error}")
else:
    print("NEGATIVE TEST FAILED")
    print("Validator accepted an unsupported DBX alignment claim.")
    raise SystemExit(1)