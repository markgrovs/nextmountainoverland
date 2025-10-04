---
title: "Contact Us"
date: 2025-10-04
draft: false
---

<p>Have a question, suggestion, or just want to say hello? Use the form below!</p>

<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
  <p class="hidden">
    <label>Don't fill this out if you're human: <input name="bot-field"></label>
  </p>
  <p>
    <label>Your Name: <input type="text" name="name" required></label>
  </p>
  <p>
    <label>Your Email: <input type="email" name="email" required></label>
  </p>
  <p>
    <label>Message: <textarea name="message" required></textarea></label>
  </p>
  <p>
    <button type="submit">Send Message</button>
  </p>
</form>

<style>
  /* Basic form styling - you can expand this */
  form {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    border: 1px solid var(--border);
    border-radius: 8px;
  }
  label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
  }
  input[type="text"],
  input[type="email"],
  textarea {
    width: 100%;
    padding: 0.75rem;
    margin-bottom: 1rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    box-sizing: border-box; /* Important for padding */
  }
  textarea {
    min-height: 150px;
    resize: vertical;
  }
  button[type="submit"] {
    background-color: var(--primary);
    color: var(--button-text);
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
  }
  button[type="submit"]:hover {
    opacity: 0.9;
  }
  /* Hide the honeypot field */
  .hidden {
    display: none;
  }
</style>
