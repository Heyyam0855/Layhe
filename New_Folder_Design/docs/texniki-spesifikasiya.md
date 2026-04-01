# TEXNİKİ SPESİFİKASİYA

## 1. SİSTEM ARXİTEKTURASI

### 1.1 Ümumi Arxitektura

```
┌─────────────────┐
│  İstifadəçilər  │
└────────┬────────┘
         │
    ┌────▼─────┐
    │ Frontend │ (React.js / Vue.js)
    └────┬─────┘
         │
    ┌────▼──────┐
    │  API      │ (REST / GraphQL)
    │  Gateway  │
    └────┬──────┘
         │
    ┌────▼──────────┐
    │  Backend      │ (Node.js / .NET)
    │  Servislər    │
    └────┬──────────┘
         │
    ┌────▼──────────┐
    │  Verilənlər   │ (PostgreSQL / MongoDB)
    │  Bazası       │
    └───────────────┘
```

### 1.2 Texnologiya Stack

#### Frontend
- **Framework**: React.js 18+ və ya Vue.js 3+
- **State Management**: Redux / Vuex / Pinia
- **UI Library**: Material-UI / Ant Design / Tailwind CSS
- **HTTP Client**: Axios
- **Form Management**: React Hook Form / VeeValidate
- **Routing**: React Router / Vue Router
- **Charts**: Chart.js / Recharts
- **Date/Time**: date-fns / moment.js

#### Backend
- **Runtime**: Node.js 18+ LTS
- **Framework**: Express.js / NestJS və ya ASP.NET Core
- **API Style**: RESTful API / GraphQL
- **Authentication**: JWT (JSON Web Tokens)
- **Validation**: Joi / class-validator
- **ORM**: Prisma / TypeORM / Entity Framework
- **File Upload**: Multer / Sharp
- **Email**: Nodemailer / SendGrid
- **SMS**: Twilio / SMS.to

#### Verilənlər Bazası
- **Primary DB**: PostgreSQL 15+
- **Cache**: Redis 7+
- **Search**: Elasticsearch (optional)
- **File Storage**: AWS S3 / Azure Blob Storage

#### DevOps
- **Containerization**: Docker
- **Orchestration**: Kubernetes / Docker Swarm
- **CI/CD**: GitHub Actions / GitLab CI / Jenkins
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Error Tracking**: Sentry

---

## 2. VERİLƏNLƏR BAZASI STRUKTUR

### 2.1 Əsas Cədvəllər

#### users (İstifadəçilər)
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    department VARCHAR(100),
    position VARCHAR(100),
    employee_id VARCHAR(50) UNIQUE,
    monthly_limit DECIMAL(10,2) DEFAULT 0,
    remaining_limit DECIMAL(10,2) DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    role VARCHAR(20) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_employee_id ON users(employee_id);
```

#### categories (Kateqoriyalar)
```sql
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    name_az VARCHAR(100) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    icon VARCHAR(50),
    parent_id INTEGER REFERENCES categories(id),
    display_order INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_categories_slug ON categories(slug);
CREATE INDEX idx_categories_parent ON categories(parent_id);
```

#### products (Məhsullar)
```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES categories(id),
    name VARCHAR(255) NOT NULL,
    name_az VARCHAR(255) NOT NULL,
    description TEXT,
    description_az TEXT,
    sku VARCHAR(100) UNIQUE NOT NULL,
    barcode VARCHAR(100),
    unit VARCHAR(20) NOT NULL, -- kg, ədəd, litr
    price DECIMAL(10,2) NOT NULL,
    vat_rate DECIMAL(5,2) DEFAULT 18.00,
    stock_quantity INTEGER DEFAULT 0,
    min_stock_level INTEGER DEFAULT 10,
    image_url VARCHAR(500),
    images JSONB, -- çoxlu şəkil üçün
    nutritional_info JSONB,
    allergen_info JSONB,
    is_available BOOLEAN DEFAULT true,
    is_featured BOOLEAN DEFAULT false,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_products_sku ON products(sku);
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_availability ON products(is_available);
```

#### orders (Sifarişlər)
```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    order_number VARCHAR(50) UNIQUE NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    -- pending, confirmed, preparing, delivering, delivered, cancelled
    subtotal DECIMAL(10,2) NOT NULL,
    vat_amount DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    delivery_date DATE,
    delivery_time_slot VARCHAR(50),
    delivery_address TEXT,
    delivery_notes TEXT,
    payment_method VARCHAR(50), -- bank_transfer, cash, card
    payment_status VARCHAR(20) DEFAULT 'unpaid',
    -- unpaid, paid, refunded
    invoice_number VARCHAR(50),
    invoice_url VARCHAR(500),
    cancelled_reason TEXT,
    cancelled_at TIMESTAMP,
    confirmed_at TIMESTAMP,
    delivered_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_order_number ON orders(order_number);
CREATE INDEX idx_orders_delivery_date ON orders(delivery_date);
```

#### order_items (Sifariş Elementləri)
```sql
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(id),
    product_name VARCHAR(255) NOT NULL,
    product_sku VARCHAR(100) NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    unit VARCHAR(20) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    vat_rate DECIMAL(5,2) NOT NULL,
    vat_amount DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);
```

#### suppliers (Təchizatçılar)
```sql
CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(20),
    address TEXT,
    voen VARCHAR(20),
    bank_name VARCHAR(100),
    bank_account VARCHAR(50),
    rating DECIMAL(3,2) DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    contract_start_date DATE,
    contract_end_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### reviews (Rəylər)
```sql
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    is_approved BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_reviews_product ON reviews(product_id);
CREATE INDEX idx_reviews_user ON reviews(user_id);
```

#### notifications (Bildirişlər)
```sql
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    type VARCHAR(50) NOT NULL,
    -- order_confirmed, order_delivered, limit_warning, etc.
    title VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    data JSONB,
    is_read BOOLEAN DEFAULT false,
    read_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_notifications_user ON notifications(user_id);
CREATE INDEX idx_notifications_read ON notifications(is_read);
```

---

## 3. API ENDPOİNTLƏRİ

### 3.1 Authentication

```
POST   /api/v1/auth/register       - Qeydiyyat
POST   /api/v1/auth/login          - Giriş
POST   /api/v1/auth/logout         - Çıxış
POST   /api/v1/auth/refresh        - Token yeniləmə
POST   /api/v1/auth/forgot-password - Şifrə bərpası
POST   /api/v1/auth/reset-password  - Şifrə sıfırlama
```

### 3.2 Users

```
GET    /api/v1/users/profile       - Profil məlumatları
PUT    /api/v1/users/profile       - Profil yeniləmə
GET    /api/v1/users/limit         - Limit məlumatı
GET    /api/v1/users/orders        - İstifadəçi sifarişləri
```

### 3.3 Categories

```
GET    /api/v1/categories          - Bütün kateqoriyalar
GET    /api/v1/categories/:id      - Kateqoriya detalları
POST   /api/v1/categories          - Yeni kateqoriya (admin)
PUT    /api/v1/categories/:id      - Kateqoriya yeniləmə (admin)
DELETE /api/v1/categories/:id      - Kateqoriya silmə (admin)
```

### 3.4 Products

```
GET    /api/v1/products            - Məhsul siyahısı
       Query params: 
       - page, limit (pagination)
       - category, search (filter)
       - sort, order (sorting)
       
GET    /api/v1/products/:id        - Məhsul detalları
POST   /api/v1/products            - Yeni məhsul (admin)
PUT    /api/v1/products/:id        - Məhsul yeniləmə (admin)
DELETE /api/v1/products/:id        - Məhsul silmə (admin)
GET    /api/v1/products/featured   - Seçilmiş məhsullar
```

### 3.5 Cart

```
GET    /api/v1/cart                - Səbət məlumatları
POST   /api/v1/cart/items          - Səbətə əlavə et
PUT    /api/v1/cart/items/:id      - Səbət elementi yenilə
DELETE /api/v1/cart/items/:id      - Səbətdən sil
DELETE /api/v1/cart                - Səbəti təmizlə
```

### 3.6 Orders

```
GET    /api/v1/orders              - Sifariş siyahısı
GET    /api/v1/orders/:id          - Sifariş detalları
POST   /api/v1/orders              - Yeni sifariş yarat
PUT    /api/v1/orders/:id/cancel   - Sifarişi ləğv et
GET    /api/v1/orders/:id/invoice  - Faktura yüklə
PUT    /api/v1/orders/:id/status   - Status dəyiş (admin)
```

### 3.7 Reviews

```
GET    /api/v1/reviews             - Rəy siyahısı
POST   /api/v1/reviews             - Yeni rəy əlavə et
PUT    /api/v1/reviews/:id         - Rəyi yenilə
DELETE /api/v1/reviews/:id         - Rəyi sil
```

### 3.8 Reports (Admin)

```
GET    /api/v1/reports/dashboard   - Dashboard statistikası
GET    /api/v1/reports/orders      - Sifariş hesabatı
GET    /api/v1/reports/users       - İstifadəçi hesabatı
GET    /api/v1/reports/products    - Məhsul hesabatı
GET    /api/v1/reports/export      - Export (Excel/PDF)
```

---

## 4. TƏHLÜKƏSİZLİK

### 4.1 Autentifikasiya və Avtorizasiya

- JWT token əsaslı autentifikasiya
- Access token: 15 dəqiqə
- Refresh token: 7 gün
- Role-based access control (RBAC)
- Permission-based authorization

### 4.2 Məlumat Təhlükəsizliyi

- Şifrələr: bcrypt (10+ rounds)
- HTTPS only (TLS 1.3)
- SQL Injection qorunması (Prepared Statements)
- XSS qorunması (Input sanitization)
- CSRF qorunması (CSRF tokens)
- Rate limiting (100 req/15min per IP)
- Input validation
- Output encoding

### 4.3 Məlumat Qorunması (GDPR)

- Şəxsi məlumatların şifrələnməsi
- Data minimization
- Right to be forgotten
- Data portability
- Consent management
- Privacy by design

---

## 5. PERFORMANCE

### 5.1 Optimallaşdırma

#### Backend
- Database indexing
- Query optimization
- Connection pooling (max 20 connections)
- Caching strategy (Redis)
- Lazy loading
- Pagination (20 items per page)
- Compression (gzip)

#### Frontend
- Code splitting
- Lazy loading components
- Image optimization (WebP format)
- CDN istifadəsi
- Browser caching
- Minification & bundling
- Service Worker (PWA)

### 5.2 Performans Hədəfləri

- **First Contentful Paint**: < 1.5s
- **Time to Interactive**: < 3s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **First Input Delay**: < 100ms

---

## 6. MONİTORİNQ VƏ LOGİNG

### 6.1 Monitoring Metrikaları

- Server health (CPU, RAM, Disk)
- Response times
- Error rates
- Database connections
- Active users
- Request per minute

### 6.2 Logging

```javascript
// Log levels
- ERROR: Critical errors
- WARN: Warnings
- INFO: General info
- DEBUG: Debug information

// Log structure
{
  timestamp: "2025-11-08T10:30:00Z",
  level: "INFO",
  service: "order-service",
  userId: 123,
  action: "create_order",
  orderId: 456,
  message: "Order created successfully",
  metadata: {...}
}
```

### 6.3 Alerting

- Email alerts for critical errors
- Slack notifications for warnings
- SMS for system downtime
- Dashboard alerts

---

## 7. BACKUP VƏ DISASTER RECOVERY

### 7.1 Backup Strategiyası

- **Full backup**: Həftəlik (Bazar günü, 02:00)
- **Incremental backup**: Gündəlik (03:00)
- **Retention**: 30 gün
- **Storage**: AWS S3 / Azure Blob (Geo-redundant)
- **Encryption**: AES-256

### 7.2 Disaster Recovery

- **RTO (Recovery Time Objective)**: 4 saat
- **RPO (Recovery Point Objective)**: 24 saat
- **Backup testing**: Aylıq
- **Disaster recovery drill**: Rüblük

---

## 8. SCALABILITY

### 8.1 Horizontal Scaling

- Load balancer (Nginx / HAProxy)
- Multiple application instances
- Database replication (Master-Slave)
- Stateless architecture
- Microservices ready

### 8.2 Vertical Scaling

- Server upgrade path
- Database optimization
- Code optimization
- Resource monitoring

---

## 9. DEPENDENCİLƏR

### 9.1 Frontend Dependencies

```json
{
  "react": "^18.2.0",
  "react-router-dom": "^6.10.0",
  "axios": "^1.4.0",
  "redux": "^4.2.1",
  "react-redux": "^8.0.5",
  "@mui/material": "^5.13.0",
  "chart.js": "^4.3.0",
  "date-fns": "^2.30.0",
  "formik": "^2.4.0",
  "yup": "^1.2.0"
}
```

### 9.2 Backend Dependencies

```json
{
  "express": "^4.18.2",
  "pg": "^8.11.0",
  "jsonwebtoken": "^9.0.0",
  "bcrypt": "^5.1.0",
  "joi": "^17.9.2",
  "nodemailer": "^6.9.3",
  "multer": "^1.4.5-lts.1",
  "redis": "^4.6.7",
  "winston": "^3.9.0"
}
```

---

## 10. VERSİYA İDARƏETMƏSİ

### 10.1 Git Strategy

- **Main branch**: Production code
- **Develop branch**: Development code
- **Feature branches**: feature/feature-name
- **Hotfix branches**: hotfix/bug-description
- **Release branches**: release/v1.0.0

### 10.2 Versioning

Semantic Versioning (SemVer): MAJOR.MINOR.PATCH

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

---

**Texniki Spesifikasiya Versiyası**: 1.0  
**Son Yeniləmə**: 08.11.2025  
**Status**: Aktiv





