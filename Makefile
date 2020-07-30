default:
	@echo "[Docker] Building docker images with distroless"
	@docker build -t ${username}/simple-web:distroless-$$(cat src/VERSION) -f images/distroless/Dockerfile .
	@echo "[Docker] Building docker images with alpine"
	@docker build -t ${username}/simple-web:alpine312-$$(cat src/VERSION) -f images/alpine/Dockerfile .
