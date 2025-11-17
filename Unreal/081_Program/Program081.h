// Camera
// Program 081

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program081.generated.h"

UCLASS()
class AProgram081 : public AActor
{
    GENERATED_BODY()

public:
    AProgram081();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
