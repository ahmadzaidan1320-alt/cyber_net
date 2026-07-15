<?php if ($error_message): ?>
        <div class="error">
            <?= htmlspecialchars($error_message) ?>
        </div>
        <?php endif; ?>

        <?php if ($login_success): ?>
        <div class="success">Login berhasil! Mengarahkan ke dashboard...</div>
        <?php else: ?>
        <form method="post" id="loginForm">
            <label for="pw">Password</label>
            <div class="input-wrap">
                <input type="password" id="pw" name="password" autocomplete="current-password" autofocus required>
                <button type="button" class="toggle-pw" onclick="togglePw()" title="Lihat password">👁</button>
            </div>
            <button type="submit" class="btn" id="submitBtn">
                <span id="btnText">Masuk</span>
            </button>
        </form>

        <div class="forgot-pw">
            <a href="#" onclick="alert('Hubungi admin untuk reset password')">Lupa Password?</a>
        </div>
        <?php endif; ?>
    </div>