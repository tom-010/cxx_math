# Install Bazel watcher: https://github.com/bazelbuild/bazel-watcher
# Pick useful scripts from here: https://github.com/cartographer-project/cartographer/tree/master/scripts

echo "install prerequisites"
sudo apt install -y python

echo "installing bazel..."
sudo apt install apt-transport-https curl gnupg
curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg
sudo mv bazel.gpg /etc/apt/trusted.gpg.d/
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
sudo apt update && sudo apt install -y bazel


echo "installing bazel watcher..."
mkdir tmp
cd tmp 
git clone https://github.com/bazelbuild/bazel-watcher
cd bazel-watcher
git checkout v0.15.10
bazel build //ibazel
sudo cp ./bazel-bin/ibazel/linux_amd64_stripped/ibazel /usr/bin/
cd ../..
rm tmp -rf