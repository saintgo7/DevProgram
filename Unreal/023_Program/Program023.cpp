// Blueprint Pure

#include "Program023.h"

AProgram023::AProgram023()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram023::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Blueprint Pure ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating blueprint pure."));

    // Implement the program logic here...
}

void AProgram023::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
