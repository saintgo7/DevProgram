// Sphere Trace
// Program 088

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program088.generated.h"

UCLASS()
class AProgram088 : public AActor
{
    GENERATED_BODY()

public:
    AProgram088();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
