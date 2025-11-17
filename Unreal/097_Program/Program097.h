// Subsystem
// Program 097

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program097.generated.h"

UCLASS()
class AProgram097 : public AActor
{
    GENERATED_BODY()

public:
    AProgram097();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
