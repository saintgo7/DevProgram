// Material Instance

#include "Program067.h"

AProgram067::AProgram067()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram067::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Material Instance ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating material instance."));

    // Implement the program logic here...
}

void AProgram067::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
