<?php
// submit.php
// Miracle Wealth Contact Form Submission to Wetroo CRM

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and collect input data
    $name = htmlspecialchars($_POST['name'] ?? '');
    $phone = htmlspecialchars($_POST['phone'] ?? '');
    $email = htmlspecialchars($_POST['email'] ?? '');
    $city = htmlspecialchars($_POST['city'] ?? '');
    $service = htmlspecialchars($_POST['service'] ?? '');
    $message = htmlspecialchars($_POST['message'] ?? '');

    // =========================================================
    // WETROO CRM WEBHOOK INTEGRATION
    // =========================================================
    $wetroo_webhook_url = getenv('WETROO_WEBHOOK_URL') ?: 'https://app.wetroo.com/incoming-webhook/8sxwv6uTVvl7goGXxQ==';

    // Map website fields to Wetroo Webhook fields
    // Wetroo expects: name, email, phone, company, address, message
    $data = [
        'name'    => $name,
        'email'   => $email,
        'phone'   => $phone,
        'company' => "Service: " . $service, // Using company field for Service
        'address' => $city,                // Using address field for City
        'message' => $message              // The actual message
    ];

    $payload = json_encode($data);

    // Initialize cURL call
    $ch = curl_init($wetroo_webhook_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Content-Length: ' . strlen($payload)
    ]);

    // Prevent SSL issues on local servers
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); 

    // Execute API Call
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    // =========================================================
    // SUCCESS REDIRECT
    // =========================================================
    header("Location: thank-you.html");
    exit();
} else {
    // Fallback if accessed without POST
    header("Location: contact.html");
    exit();
}
?>
