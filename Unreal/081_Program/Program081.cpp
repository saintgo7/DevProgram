// Camera

#include "Program081.h"

AProgram081::AProgram081()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram081::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Camera ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating camera."));

    // Implement the program logic here...
}

void AProgram081::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
