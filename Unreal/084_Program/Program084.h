// Camera Shake
// Program 084

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program084.generated.h"

UCLASS()
class AProgram084 : public AActor
{
    GENERATED_BODY()

public:
    AProgram084();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
