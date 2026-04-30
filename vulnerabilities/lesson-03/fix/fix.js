// Lesson 3 — Fix
// Safe parsing and allowlist validation prevent malicious action values.

var req = JSON.parse(event.body);
var headers = event.headers;
var auth_header = headers.Authorization || headers.authorization;
var action = req.action;

const allowedActions = [
  "new", "update", "cancel", "get", "orders",
  "account", "profile", "shipping", "billing",
  "complete", "inbox", "message", "delete",
  "upload", "feedback", "admin-orders"
];

if (!allowedActions.includes(action)) {
  return callback(null, {
    statusCode: 400,
    headers: { "Access-Control-Allow-Origin": "*" },
    body: JSON.stringify({ status: "err", message: "Invalid action" })
  });
}