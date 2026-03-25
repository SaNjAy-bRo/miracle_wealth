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
    // WETROO CRM API INTEGRATION
    // IMPORTANT: Replace the Endpoint and API key below
    // with the exact credentials from your Wetroo CRM dashboard.
    // =========================================================
    $wetroo_endpoint = 'https://api.wetroo.com/v1/lead/create'; // Change if different
    $wetroo_api_key = 'YOUR_WETROO_API_KEY_HERE';

    $data = [
        'api_key' => $wetroo_api_key,
        'name'    => $name,
        'mobile'  => $phone,       // Often mapped to 'mobile' or 'phone'
        'email'   => $email,
        'city'    => $city,
        'service' => $service,
        'remarks' => $message,
        'source'  => 'Website Contact Form'
    ];

    // Initialize cURL call
    $ch = curl_init($wetroo_endpoint);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));

    // Prevent SSL issues on local servers, but better to keep true on production
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); 

    // Execute API Call
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    // =========================================================
    // SUCCESS REDIRECT
    // Redirects user to Thank You page after successful POST
    // =========================================================
    header("Location: thank-you.html");
    exit();
} else {
    // Fallback if accessed without POST
    header("Location: contact.html");
    exit();
}
?>
