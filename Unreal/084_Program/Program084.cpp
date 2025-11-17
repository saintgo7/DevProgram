// Camera Shake

#include "Program084.h"

AProgram084::AProgram084()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram084::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Camera Shake ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating camera shake."));

    // Implement the program logic here...
}

void AProgram084::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
