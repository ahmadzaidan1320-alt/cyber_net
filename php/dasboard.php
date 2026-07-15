<?php
session_start();
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    header("Location: index.php");
    exit;
}
?>
<!DOCTYPE html>
<html>

<head>
    <title>Dashboard - cyber_net</title>
</head>

<body style="background: #0f1117; color: white; padding: 50px; font-family: Arial;">
    <h1>🎉 Selamat Datang di Dashboard Admin!</h1>
    <p>Login berhasil pada: <?= date('d/m/Y H:i:s', $_SESSION['login_time']) ?></p>
    <a href="logout.php" style="color: #0841eb;">Logout</a>
</body>

</html>
<?php
session_start();
session_destroy();
header("Location: index.php");
exit;
?>
<?php
session_start();
header('Content-Type: application/json');
echo json_encode([
    'redirect' => isset($_SESSION['logged_in']) && $_SESSION['logged_in'] === true
]);
?>