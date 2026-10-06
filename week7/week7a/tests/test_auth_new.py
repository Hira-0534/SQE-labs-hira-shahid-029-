import pytest
import auth


@pytest.fixture(autouse=True)
def reset_auth_store():
    auth.initialize_store()
# TC-008: login with unregistered email (REQ-01)
def test_login_rejects_unknown_user():
    result = auth.validate_login("unknown@uni.edu", "ValidPass1")

    assert result["success"] is False
    assert result["user_id"] is None
    assert result["error"] == "Invalid credentials"


# TC-009: login rejected when account is already locked (REQ-02)
def test_login_rejects_locked_account():
    auth.lock_account("student@uni.edu")

    result = auth.validate_login("student@uni.edu", "ValidPass1")

    assert result["success"] is False
    assert result["user_id"] == "STU-001"
    assert result["error"] == "Account is locked"


# TC-010: account is locked after 3 wrong passwords (REQ-02)
def test_login_locks_account_after_3_wrong_passwords():
    auth.validate_login("student@uni.edu", "WrongPass1")
    auth.validate_login("student@uni.edu", "WrongPass2")
    
    result = auth.validate_login("student@uni.edu", "WrongPass3")

    assert result["success"] is False
    assert result["error"] == "Invalid credentials"
    assert auth.is_locked("student@uni.edu") is True
# TC-011: check lockout for already locked account
def test_check_lockout_when_account_already_locked():
    auth.lock_account("student@uni.edu")

    result = auth.check_lockout("student@uni.edu", attempt_count=0)

    assert result is False


# TC-012: check lockout when attempt count reaches maximum
def test_check_lockout_at_max_attempts():
    result = auth.check_lockout("student@uni.edu", attempt_count=3)

    assert result is False
    assert auth.is_locked("student@uni.edu") is True


# TC-013: check lockout for unknown user with max attempts
def test_check_lockout_unknown_user_at_max_attempts():
    result = auth.check_lockout("unknown@uni.edu", attempt_count=3)

    assert result is False


# TC-014: check lockout when attempts are below maximum
def test_check_lockout_allows_attempts_below_limit():
    result = auth.check_lockout("student@uni.edu", attempt_count=1)

    assert result is True


# TC-015: lock an existing account
def test_lock_account():
    auth.lock_account("student@uni.edu")

    assert auth.is_locked("student@uni.edu") is True


# TC-016: unlock an account and reset attempts
def test_unlock_account():
    auth.lock_account("student@uni.edu")
    auth.unlock_account("student@uni.edu")

    assert auth.is_locked("student@uni.edu") is False


# TC-017: unlock unknown account
def test_unlock_unknown_account():
    auth.unlock_account("unknown@uni.edu")

    assert auth.is_locked("unknown@uni.edu") is False


# TC-018: reset failed attempt count
def test_reset_attempt_count():
    auth.validate_login("student@uni.edu", "WrongPass1")
    auth.reset_attempt_count("student@uni.edu")

    result = auth.validate_login("student@uni.edu", "WrongPass2")

    assert result["success"] is False
    assert auth.is_locked("student@uni.edu") is False


# TC-019: reset attempts for unknown user
def test_reset_attempt_count_unknown_user():
    auth.reset_attempt_count("unknown@uni.edu")


# TC-020: check is_locked for unknown user
def test_is_locked_unknown_user():
    assert auth.is_locked("unknown@uni.edu") is False


# TC-021: destroy existing session
def test_destroy_existing_session():
    auth.create_session("STU-001")

    auth.destroy_session("STU-001")

    assert auth.is_session_valid("STU-001") is False


# TC-022: destroy non-existing session
def test_destroy_non_existing_session():
    auth.destroy_session("STU-999")


# TC-023: session does not exist
def test_session_invalid_when_not_created():
    assert auth.is_session_valid("STU-999") is False


# TC-024: valid session
def test_valid_session():
    auth.create_session("STU-001", idle_minutes=5)

    assert auth.is_session_valid("STU-001") is True


# TC-025: update existing session activity
def test_update_session_activity():
    auth.create_session("STU-001", idle_minutes=10)

    auth.update_session_activity("STU-001")

    assert auth.is_session_valid("STU-001") is True


# TC-026: update non-existing session
def test_update_non_existing_session():
    auth.update_session_activity("STU-999")


# TC-027: handle session creates new session
def test_handle_session_creates_new_session():
    result = auth.handle_session("STU-001")

    assert result is True


# TC-028: handle existing valid session
def test_handle_existing_valid_session():
    auth.create_session("STU-001", idle_minutes=5)

    result = auth.handle_session("STU-001")

    assert result is True


# TC-029: handle expired session
def test_handle_expired_session():
    auth.create_session("STU-001", idle_minutes=31)

    result = auth.handle_session("STU-001")

    assert result is False


# TC-030: generate reset token
def test_generate_reset_token():
    token = auth.generate_reset_token("student@uni.edu")

    assert token is not None
    assert auth.verify_reset_token(token) is True


# TC-031: verify unknown reset token
def test_verify_unknown_reset_token():
    result = auth.verify_reset_token("invalid-token")

    assert result is False


# TC-032: verify expired reset token
def test_verify_expired_reset_token():
    token = auth.generate_reset_token("student@uni.edu", hours_ago=2)

    assert auth.verify_reset_token(token) is False


# TC-033: used reset token is rejected
def test_used_reset_token():
    token = auth.generate_reset_token("student@uni.edu")

    auth.mark_token_used(token)

    assert auth.verify_reset_token(token) is False


# TC-034: mark unknown token as used
def test_mark_unknown_token_used():
    auth.mark_token_used("unknown-token")


# TC-035: reset email for unknown user
def test_reset_email_unknown_user():
    result = auth.send_reset_email("unknown@uni.edu")

    assert result["sent"] is False
    assert result["error"] == "Email address not found"


# TC-036: reset email rate limit
def test_reset_email_rate_limit():
    for _ in range(3):
        result = auth.send_reset_email("student@uni.edu")
        assert result["sent"] is True

    result = auth.send_reset_email("student@uni.edu")

    assert result["sent"] is False
    assert result["error"] == "Rate limit exceeded"


# TC-037: reset email handles token generation failure
def test_reset_email_token_generation_failure(monkeypatch):

    def fake_generate_token(email):
        raise Exception("Token error")

    monkeypatch.setattr(auth, "generate_reset_token", fake_generate_token)

    result = auth.send_reset_email("student@uni.edu")

    assert result["sent"] is False
    assert "Token generation failed" in result["error"]


# TC-038: reset email handles SMTP failure
def test_reset_email_smtp_failure(monkeypatch):

    def fake_deliver_email(email, token):
        raise ConnectionError("SMTP connection failed")

    monkeypatch.setattr(auth, "_deliver_email", fake_deliver_email)

    result = auth.send_reset_email("student@uni.edu")

    assert result["sent"] is False
    assert "SMTP error" in result["error"]

