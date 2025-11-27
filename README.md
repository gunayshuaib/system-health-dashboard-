# System Health Dashboard

A lightweight Flask dashboard displaying real‑time CPU and memory usage. Includes:

* Docker & Docker Compose
* Kubernetes manifests
* Helm chart
* GitHub Actions CI/CD
* Live charts (Chart.js)

---

## 🚀 Run Locally

```bash
docker build -t system-health-dashboard .
docker run -p 5000:5000 system-health-dashboard
```

App: [http://localhost:5000](http://localhost:5000)

---

## 🐳 Docker Compose

```bash
docker-compose up --build
```

---

## ☸️ Kubernetes Deployment

### 1. Apply manifests

Edit image in `k8s/deployment.yaml`, then:

```bash
kubectl apply -f k8s/
```

### 2. Verify

```bash
kubectl get pods -l app=system-health-dashboard
kubectl get svc system-health-dashboard
```

### 3. Port‑forward (if no ingress)

```bash
kubectl port-forward deployment/system-health-dashboard 5000:5000
```

---

## 🛳 Helm Chart Deployment

### 1. Install / Upgrade

```bash
helm upgrade --install system-health-dashboard charts/system-health-dashboard \
  --set image.repository=ghcr.io/ORG/REPO \
  --set image.tag=latest
```

### 2. Check resources

```bash
kubectl get all -l app=system-health-dashboard
```

---

## 🔄 GitHub Actions CI/CD

Pipeline builds & pushes the Docker image → deploys via Helm.

### Requirements:

* Secret `KUBECONFIG` (base64 kubeconfig)

### How to generate:

```bash
base64 ~/.kube/config | pbcopy
```

Add result to GitHub repo secrets as `KUBECONFIG`.

---

## 📊 UI

Accessible at service or ingress URL.
Charts auto-refresh using `/metrics` endpoint.

---

## 🧹 Cleanup

```bash
helm uninstall system-health-dashboard
kubectl delete -f k8s/
```

---

## Notes

* Replace `ghcr.io/ORG/REPO` with your actual GHCR path.
* If using Minikube: `minikube service system-health-dashboard --url`
