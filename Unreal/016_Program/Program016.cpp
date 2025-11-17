// UObject

#include "Program016.h"

AProgram016::AProgram016()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram016::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== UObject ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating uobject."));

    // Implement the program logic here...
}

void AProgram016::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
