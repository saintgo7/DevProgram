// Spring Arm

#include "Program083.h"

AProgram083::AProgram083()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram083::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Spring Arm ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating spring arm."));

    // Implement the program logic here...
}

void AProgram083::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
