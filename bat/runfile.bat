cd C:\Users\ColesSA\Documents\Github\PastPort\PastPortApi - Docker
docker build . -t api:release
echo "Build Complete!"
call docker run -p 5000:5000 -it api:release