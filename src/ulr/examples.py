"""Running example of the paper (§2, Fig. 3, Appendices A and B): Young v. Hitchens."""
from __future__ import annotations

from .components import Fact, Hypothesis, Issue, Outcome, Precedent, Theory

ISSUE = Issue(
    claim="the defendant is guilty of theft",
    negated_claim="the defendant is not guilty of theft",
    theory_head="A person is typically guilty of theft if the following conditions hold:",
)

# Facts of Young v. Hitchens as used in the prompts (facts 1-2; fact 3 is the claim itself).
YOUNG_V_HITCHENS = Fact(
    name="Young v. Hitchens",
    statements=[
        "The plaintiff was fishing with a net in an open sea.",
        "While the net was almost closed, the defendant rowed his boat, entered the net, "
        "caught the fish, and rowed his boat out of the net with the fish.",
    ],
)

# (Fictional) civil-law proof structure (§2, Appendix A).
CIVIL_THEORY = Theory(
    head="A person is guilty of theft if:",
    conditions=[
        "the person committed an action to take away the object,",
        "the object belonged to another person,",
        "the person knew that the object belonged to the other person, and",
        "the person had an intention to take away the object",
    ],
    exception="The rule is not applicable if the purpose of taking away is to prevent dangers.",
)

KEEBLE_V_HICKERINGILL = Precedent(
    name="Keeble v. Hickeringill",
    fact=Fact(
        name="Keeble v. Hickeringill",
        statements=[
            "The plaintiff owned land containing a pond, where the plaintiff always takes ducks for a profit.",
            "The defendant, knowing about the decoy pond, fired the guns to scare away the ducks in the pond.",
        ],
    ),
    outcome=Outcome(ISSUE, True),
)

PIERSON_V_POST = Precedent(
    name="Pierson v. Post",
    fact=Fact(
        name="Pierson v. Post",
        statements=[
            "The plaintiff chased a fox in an open land.",
            "The defendant killed it and carried it away.",
        ],
    ),
    outcome=Outcome(ISSUE, False),
)

PRECEDENTS = {"plaintiff": KEEBLE_V_HICKERINGILL, "defendant": PIERSON_V_POST}

# Theories produced by the case-based step in Appendix B.1 (used as fixed inputs in the evaluation tasks).
PLAINTIFF_THEORY = Theory(
    head="A person is typically guilty of theft if the following conditions hold:",
    conditions=[
        "They intentionally and without consent take possession of another person's property.",
        "That property has economic value to the owner and is considered personal property.",
    ],
)
DEFENDANT_THEORY = Theory(
    head="A person is typically guilty of theft if the following conditions hold:",
    conditions=[
        "They unlawfully appropriate property belonging to another.",
        "That property is considered tangible and has been reduced to possession by the owner.",
    ],
)

# Hypotheses accepted by the judge in Appendix A.3 / B.3.
A3_HYPOTHESIS = Hypothesis(
    statement="The fish were still in the common resource of the open sea until that point, "
    "and therefore not yet the property of the plaintiff.",
    side="defendant",
)
B3_HYPOTHESIS = Hypothesis(
    statement="The fish were not yet in the plaintiff's possession as the fish were still in the open sea "
    "and the plaintiff hadn't yet physically secured them.",
    side="defendant",
)

# Keywords that make a scripted judge reproduce the paper's choice (accept the defendant's hypothesis).
PAPER_JUDGE_KEYWORDS = ("possession", "common resource", "not yet")
