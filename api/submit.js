
export default async function handler(req, res) {
  // Only allow POST requests
  if (req.method !== 'POST') {
    res.setHeader('Allow', ['POST']);
    return res.status(405).end(`Method ${req.method} Not Allowed`);
  }

  // Parse body (Vercel automatically parses application/x-www-form-urlencoded)
  const { name, email, phone, city, service, message } = req.body;
  const webhookUrl = process.env.WETROO_WEBHOOK_URL || 'https://app.wetroo.com/incoming-webhook/8sxwv6uTVvl7goGXxQ==';

  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name,
        email,
        phone,
        company: `Service: ${service || 'General Enquiry'}`,
        address: city || 'Not Provided',
        message: message || 'No message provided'
      }),
    });

    if (response.ok) {
      // Successful redirect to thank you page
      return res.redirect(302, '/thank-you.html');
    } else {
      console.error('Wetroo CRM responded with error:', response.status);
      return res.redirect(302, '/contact.html?error=crm_failed');
    }
  } catch (error) {
    console.error('Fetch error:', error);
    return res.redirect(302, '/contact.html?error=server_error');
  }
}
